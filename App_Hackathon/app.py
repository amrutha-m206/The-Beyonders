import time
import streamlit as st
from groq import Groq


client = Groq(api_key="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")


def get_meditation_prompt(stage, duration):
    try:
        system_prompt = """
        You are a meditation guide. Generate helpful and soothing prompts for the user based on the stage of their meditation. 
        The meditation should encourage relaxation, mindfulness, and focus, ensuring the user feels calm and centered.
        Provide the prompt as a clear, concise sentence.
        """
        prompt = f"Generate a meditation instruction for stage {stage} of a {duration}-minute meditation session."
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=100,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating prompt: {str(e)}"


def guided_meditation_with_llama():
    duration = st.session_state.meditation_duration
    progress_bar = st.progress(st.session_state.elapsed_time / (duration * 60))
    meditation_text = st.empty()

    while st.session_state.elapsed_time < duration * 60:
        meditation_prompt = get_meditation_prompt(
            st.session_state.meditation_stage, duration
        )
        meditation_text.write(meditation_prompt)
        progress_bar.progress(st.session_state.elapsed_time / (duration * 60))

        time.sleep(15)

        st.session_state.elapsed_time += 15
        st.session_state.meditation_stage += 1

    meditation_text.write(
        "Meditation complete. Slowly open your eyes when you're ready."
    )
    progress_bar.progress(1.0)


def mental_health_query_bot():
    try:
        system_prompt = """
        You are a mental health assistant. Provide helpful, kind, and informative responses to mental health-related queries.
        Your responses should be empathetic, supportive, and based on scientific knowledge of mental health.
        If you do not know the answer, say 'I am not sure, but you might want to speak with a professional.'
        """
        prompt = f"User asks: {st.session_state.query}"
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            model="llama3-8b-8192",
            temperature=0.7,
            max_tokens=470,
        )
        st.session_state.query_answer = completion.choices[0].message.content
    except Exception as e:
        st.session_state.query_answer = f"Error answering query: {str(e)}"


def main():

    if "query_answer" not in st.session_state:
        st.session_state.query_answer = ""
    if "query" not in st.session_state:
        st.session_state.query = ""
    if "show_resources" not in st.session_state:
        st.session_state.show_resources = False
    if "meditation_stage" not in st.session_state:
        st.session_state.meditation_stage = 1
    if "elapsed_time" not in st.session_state:
        st.session_state.elapsed_time = 0
    if "meditation_duration" not in st.session_state:
        st.session_state.meditation_duration = 5

    st.title("Mental Health Support")

    if st.button("Start Guided Meditation"):
        guided_meditation_with_llama()

    st.subheader("Ask Mental Health Question")
    st.session_state.query = st.text_input("Type your question:")
    if st.button("Get Answer"):
        mental_health_query_bot()

    # Display Answer
    if st.session_state.query_answer:
        st.subheader("Response")
        st.write(st.session_state.query_answer)

    # Resources Section - Button Controlled
    if st.button("Show Mental Health Resources"):
        st.session_state.show_resources = True

    if st.session_state.show_resources:
        st.subheader("Helpful Mental Health Resources")
        resources = [
            {
                "name": "National Suicide Prevention Lifeline",
                "url": "https://suicidepreventionlifeline.org/",
            },
            {
                "name": "Mindfulness Exercises",
                "url": "https://mindfulnessexercises.com/",
            },
            {
                "name": "BetterHelp (Online Therapy)",
                "url": "https://www.betterhelp.com/",
            },
        ]
        for resource in resources:
            st.markdown(f"- [{resource['name']}]({resource['url']})")


if __name__ == "__main__":
    main()
