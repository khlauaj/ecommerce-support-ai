"""
Day 7：下載 Bitext 數據集、數意圖、分開 few-shot 池同 eval 池

用法（喺 repo 根目錄行）：
    python prepare_data.py

產出：
    data/fewshot_pool.csv  —— 只可以放入 prompt 做例子
    data/eval_pool.csv     —— 只可以用嚟考試，永遠唔好放入 prompt
"""
from pathlib import Path

import pandas as pd

DATASET = "bitext/Bitext-customer-support-llm-chatbot-training-dataset"
FEWSHOT_PER_INTENT = 5   # 每個意圖放幾多條入 few-shot 池
EVAL_PER_INTENT = 8      # 每個意圖放幾多條入 eval 池
SEED = 42                # 固定隨機種子：每次行都抽到同一批，結果先可以比較
OUT_DIR = Path("data")


def load_bitext() -> pd.DataFrame:
    from datasets import load_dataset
    return load_dataset(DATASET, split="train").to_pandas()


def describe(df: pd.DataFrame) -> None:
    print(f"總行數：{len(df):,}")
    print(f"欄位：{df.columns.tolist()}")
    print(f"類別數目：{df['category'].nunique()}")
    print(f"意圖數目：{df['intent'].nunique()}\n")

    print("每個類別有咩意圖：")
    for category, group in df.groupby("category"):
        intents = sorted(group["intent"].unique())
        print(f"  {category} ({len(intents)})：{', '.join(intents)}")

    counts = df["intent"].value_counts()
    print(f"\n每個意圖最少 {counts.min()} 條，最多 {counts.max()} 條")


def split_pools(df: pd.DataFrame, n_fewshot: int, n_eval: int, seed: int):
    """先將全部數據隨機打亂，再喺每個意圖入面編號：
    頭 n_fewshot 條做 few-shot，跟住 n_eval 條做 eval。
    同一條數據只會出現喺其中一個池，保證唔會「漏題」。"""
    n_total = n_fewshot + n_eval
    shuffled = df.sample(frac=1, random_state=seed).reset_index(drop=True)
    rank = shuffled.groupby("intent").cumcount()
    fewshot = shuffled[rank < n_fewshot]
    eval_pool = shuffled[(rank >= n_fewshot) & (rank < n_total)]
    return (
        fewshot.sort_values("intent").reset_index(drop=True),
        eval_pool.sort_values("intent").reset_index(drop=True),
    )


def check_no_leak(fewshot: pd.DataFrame, eval_pool: pd.DataFrame) -> None:
    overlap = set(fewshot["instruction"]) & set(eval_pool["instruction"])
    if overlap:
        raise ValueError(f"有 {len(overlap)} 條查詢同時出現喺兩個池，請檢查！")
    print("檢查通過：兩個池冇重複嘅查詢")


def main() -> None:
    df = load_bitext()
    describe(df)

    fewshot, eval_pool = split_pools(df, FEWSHOT_PER_INTENT, EVAL_PER_INTENT, SEED)
    check_no_leak(fewshot, eval_pool)

    OUT_DIR.mkdir(exist_ok=True)
    fewshot.to_csv(OUT_DIR / "fewshot_pool.csv", index=False)
    eval_pool.to_csv(OUT_DIR / "eval_pool.csv", index=False)
    print(f"\nfew-shot 池：{len(fewshot)} 條 → {OUT_DIR / 'fewshot_pool.csv'}")
    print(f"eval 池：{len(eval_pool)} 條 → {OUT_DIR / 'eval_pool.csv'}")


if __name__ == "__main__":
    main()
