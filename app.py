from functions import soundToMedianFrequency, possibleRange, soundToSustainedFrequency, possibleRangeForMedian, recording
import streamlit as st 


st.title("Vocal Range Analyzer")
st.write("Use 3 samples to estimate vocal range.")

# Initiate stage 
if 'stage' not in st.session_state:
    st.session_state.stage = 1
    st.session_state.data = {}

# RECORD NOTE 
if st.session_state.stage == 1: 
    st.header("Hum your highest note: ")
    audio_high = st.audio_input("Record", key="rec_high")
    if audio_high: 
        st.session_state.data['high'] = soundToMedianFrequency(audio_high) 
        if st.button('Next', key="btn_1"):
            st.session_state.stage = 2
            st.rerun()

elif st.session_state.stage == 2: 
    st.header("Hum your lowest note")
    audio_low = st.audio_input("Record")
    if audio_low: 
        st.session_state.data['low'] = soundToMedianFrequency(audio_low)
        st.session_state.data['possibilities'] = possibleRange(st.session_state.data['high'], st.session_state.data['low'])
        if st.button('Next', key="btn_2"):
            st.session_state.stage = 3
            st.rerun()


elif st.session_state.stage == 3: 
    st.header("Shout 'Hey' 3 times as if you were calling a person afar")
    audio_sustained = st.audio_input("Record")
    if audio_sustained: 
        st.session_state.data['sustained'] = soundToSustainedFrequency(audio_sustained)
        if st.button("Analyze result", key="btn_3"):
            st.session_state.stage = 4
            st.rerun()

elif st.session_state.stage == 4:
    result = possibleRangeForMedian(st.session_state.data['possibilities'], st.session_state.data['sustained'])
    st.success(f"Analysis Complete! Your vocal range is: {result}")

    st.balloons()

# print("Hum your highest note: ")
# highestSound = recording()

# print("Hum your lowest note: ")
# lowestSound = recording()

# print("Shout 'Hey' 3 times as if you were calling a person from afar: ")
# sustainedSound = recording()

# # Analyze vocal range 
# print("Analyzing your vocal range ... ")

# highestNote = soundToMedianFrequency(highestSound)
# lowestNote = soundToMedianFrequency(lowestSound)

# possibilities = possibleRange(highestNote, lowestNote)

# sustainedNote = soundToSustainedFrequency(sustainedSound)
# print("Your vocal range is likely: ")
# print(possibleRangeForMedian(possibilities, sustainedNote))




