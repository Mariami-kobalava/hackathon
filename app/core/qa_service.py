from app.core.avatar import generate_avatar_response

# Simple sample questions + video URLs
qa_data = {
    "When does the semester start?": "The semester starts on September 1st.",
    "How can I contact administration?": "You can contact administration via email admin@university.com.",
    "What are the library hours?": "Library is open 8AM to 10PM daily."
}

def get_answer_with_video(question: str):
    # Get text answer
    answer = qa_data.get(question, "Sorry, I don't have an answer for that.")

    # Generate D-ID video
    try:
        avatar_response = generate_avatar_response("admin", answer)

        if avatar_response.get('status') == 'done':
            return {
                "answer": answer,
                "video_url": avatar_response.get('video_url'),
                "status": "success"
            }
        else:
            # D-ID failed or timed out
            return {
                "answer": answer,
                "video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4",
                "status": "fallback",
                "did_error": avatar_response
            }
    except Exception as e:
        # Fallback to static response if D-ID fails
        return {
            "answer": answer,
            "video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4",
            "status": "error",
            "error": str(e)
        }
