import giphy
import os
from atproto import Client
from datetime import datetime, timezone

client = Client()
client.login(os.environ['BLUESKY_USERNAME'], os.environ['BLUESKY_PASSWORD'])

# Get notifications (mentions, replies, etc.)
notifications_response = client.app.bsky.notification.list_notifications(params={'limit': 50})
notifications = notifications_response.notifications

# Filter for mentions that contain "hug" keywords
hug_keywords = ['hug', 'hugs', 'hugging', 'need a hug', 'could use a hug']
reply_targets = []

for notification in notifications:
    # Check if it's a mention and contains hug-related keywords
    if (notification.reason == 'mention' and 
        notification.record and 
        hasattr(notification.record, 'text')):
        
        text_lower = notification.record.text.lower()
        if any(keyword in text_lower for keyword in hug_keywords):
            
            # Check if we've already replied to this post
            try:
                thread_response = client.app.bsky.feed.get_post_thread(params={'uri': notification.uri})
                post_thread = thread_response.thread
                
                # Check if we've already replied
                already_replied = False
                if hasattr(post_thread, 'replies') and post_thread.replies:
                    our_handle = client.me.handle
                    for reply in post_thread.replies:
                        if (hasattr(reply, 'post') and 
                            hasattr(reply.post, 'author') and 
                            reply.post.author.handle == our_handle):
                            already_replied = True
                            print(f"Already replied to @{notification.author.handle}, skipping...")
                            break
                
                if not already_replied:
                    reply_targets.append({
                        'uri': notification.uri,
                        'cid': notification.cid,
                        'author': notification.author.handle,
                        'text': notification.record.text[:50] + '...' if len(notification.record.text) > 50 else notification.record.text
                    })
                    
            except Exception as e:
                print(f"Error checking replies for @{notification.author.handle}: {e}")
                # If we can't check replies, skip to be safe
                continue

for i, target in enumerate(reply_targets, start=1):
    try:
        video_filename, alt_text = giphy.download_random_gif()
        
        with open(video_filename, 'rb') as f:
            video_data = f.read()
            
        # Create reply post with video
        reply_ref = {
            'root': {'uri': target['uri'], 'cid': target['cid']},
            'parent': {'uri': target['uri'], 'cid': target['cid']}
        }
        
        client.send_video(
            text="🤗",  # Simple hug emoji as reply text
            video=video_data,
            video_alt=alt_text or "A random hug GIF to brighten your day!",
            reply_to=reply_ref
        )
        
        print(f"Replied to post {i} from @{target['author']}: {target['text']}")
        
    except Exception as e:
        print(f"An error occurred while replying to post from @{target['author']}: {e}")
    finally:
        if 'video_filename' in locals() and os.path.exists(video_filename):
            os.remove(video_filename)
