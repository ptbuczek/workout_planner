import polars as pl
import streamlit as st

st.markdown("# Plan 2 (09.2026 - )")

plan_a = pl.DataFrame(
    {
        "Number": ["1", "2", "3a", "3b", "4"],
        "Exercise": [
            "back squat",
            "biacromical bench press",
            "seated arnold press",
            "lateral raise",
            "1-arm overhead walk",
        ],
        "Reps (1st/5th week)": [
            "4x6 (5x5)",
            "4x6 (4x5)",
            "4x12 (4x8)",
            "4x10 (4x6)",
            "4x50m (4x30)",
        ],
        "Pace (1st/5th week)": [
            "4010 (2010)",
            "3010 (2010)",
            "2010 (3010)",
            "1010 (2011)",
            "-",
        ],
        "Break (in sec)": ["120-180", "120-180", "60", "120", "60"],
    }
)
plan_b = pl.DataFrame(
    {
        "Number": ["1", "2", "3a", "3b", "4"],
        "Exercise": [
            "chin up",
            "deadlift",
            "1-arm row",
            "trap 3 raise",
            "concentration curl",
        ],
        "Reps (1st/5th week)": [
            "4x6 (5x5)",
            "4x6 (4x4)",
            "4x12 (4x8)",
            "4x12 (4x15)",
            "4x12 (4x8)",
        ],
        "Pace (1st/5th week)": [
            "3010 (5010)",
            "3111 (4111)",
            "2010 (3010)",
            "3011",
            "2010",
        ],
        "Break (in sec)": ["120-180", "120-180", "60", "60-120", "120"],
    }
)
journal_a = pl.DataFrame(
    {
        "Number": ["1", "2", "3a", "3b", "4"],
        "Exercise": [
            "back squat",
            "biacromical bench press",
            "seated arnold press",
            "lateral raise",
            "1-arm overhead walk",
        ],
        "04/09/26 (kg)": [60, 60, 10, 5, 8],
    }
)

st.markdown(" ## Workout A")
st.dataframe(plan_a)

st.markdown(" ## Journal A")
st.dataframe(journal_a)

st.markdown(" ## Workout B")
st.dataframe(plan_b)
