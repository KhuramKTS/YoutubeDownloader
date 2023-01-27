print("Youtube Downloader - Build By @KhuramKTS")
import pytube
# Prompt user for YouTube video link
video_link = input("Enter a YouTube video link: ")
try:
    video = pytube.YouTube(video_link)
    while True:
        # Print available video and audio formats
        formats = video.streams
        for i, format in enumerate(formats):
            type = "Video" if "video" in format.mime_type else "Audio"
            progressive_tag = "- Progressive" if format.is_progressive else ""
            if type=='Video':
                info = f"{type} - {format.mime_type.split('/')[-1]} - {format.resolution} - {format.filesize_mb}MB {progressive_tag}"
            else:
                info = f"{type} - {format.mime_type.split('/')[-1]} - {format.abr} - {format.filesize_mb}MB {progressive_tag}"
            print(f"{i+1}. {info}")
    
        # Prompt user to select a format to download
        selection = int(input("Enter the number of the format you want to download: "))
    
        # Download the selected format
        video_format = formats[selection-1]
        video_format.download()
    
        print("Download complete!")
    
        # Ask user if they want to download the same video in another format
        choice = input("Do you want to download the same video in another format? (yes/no)").lower()
        if choice == 'no':
            break
        elif choice != 'yes':
            break

except Exception as e:
    print(e)

print("Youtube Downloader - Build By @KhuramKTS")
input("Press any key to exit.")
