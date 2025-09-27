# Simple sample questions + video URLs
qa_data = {
    "When does the semester start?": {
        "answer": "The semester starts on September 1st.",
        "video_url": "https://youtu.be/QLpArkPb-YU"
    },
    "How can I contact administration?": {
        "answer": "You can contact administration via email admin@university.com.",
        "video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4"
    },
    "What are the library hours?": {
        "answer": "Library is open 8AM to 10PM daily.",
        "video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4"
    }
    # შეგიძლია დაამატო დანარჩენი კითხვები + ვიდეოები აქ
}

def get_answer_with_video(question: str):
    return qa_data.get(question, {
        "answer": "Sorry, I don't have an answer for that.",
        "video_url": "https://sample-videos.com/video123/mp4/240/big_buck_bunny_240p_1mb.mp4"
    })
