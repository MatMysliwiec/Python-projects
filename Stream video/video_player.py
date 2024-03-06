import cv2
from pytube import YouTube


def download_video(url, output_path="video.mp4"):
    yt = YouTube(url)
    ys = yt.streams.filter(file_extension="mp4", progressive=True).first()
    ys.download(output_path)


def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Online Video Player", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_url = input("Enter the URL of the video: ")
    download_video(video_url)

    video_path = "video.mp4"
    play_video(video_path)
