import polars as pl
import streamlit as st

st.markdown("# Plan 1 (06.2026 - 08.2026 )")

plan_a1 = pl.DataFrame(
    {
        "Number": ["1a", "1b", "2a", "2b", "3", "4a", "4b"],
        "Exercise": [
            "trap 3 raise",
            "1-arm bottom up serratus press",
            "1-arm landmine press",
            "hammer pull-up",
            "db incline press",
            "barbell curl",
            "bar ez skull crusher",
        ],
        "Reps (1st/5th week)": [
            "3x12",
            "3x12",
            "4x8 (4x12)",
            "4x8 (4x6)",
            "3x12 (4x8)",
            "4x12 (4x8)",
            "4x12 (4x8)",
        ],
        "Pace (1st/5th week)": [
            "2011",
            "2020",
            "2010",
            "2010 (3010)",
            "3010",
            "2010",
            "3010 (4010)",
        ],
        "Break (in sec)": ["15", "60", "60", "120-180", "120", "60", "60-120"],
    }
)


st.markdown(" ## Workout A1")
st.dataframe(plan_a1)
