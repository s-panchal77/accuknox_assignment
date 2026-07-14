import time
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver

from signals_app.models import UserProfile


# This function is the signal receiver.
# Django will call it automatically every time a UserProfile is saved.
# We connect it to post_save using the @receiver decorator.
# sender=UserProfile means this only fires for UserProfile saves, not all models.
@receiver(post_save, sender=UserProfile)
def on_user_profile_saved(sender, instance, created, **kwargs):

    print("---")
    print(f"[SIGNAL] Signal received for: {instance.name}")
    print("[SIGNAL] Signal handler has started executing...")

    # --- Phase 2 Addition ---
    # Get the current thread ID where this signal is running
    signal_thread_id = threading.get_ident()
    print(f"[SIGNAL] Signal Thread ID : {signal_thread_id}")
    
    # We attach the thread ID to the instance so the caller can check it later
    instance.signal_thread_id = signal_thread_id
    # ------------------------

    # Intentional 2-second delay.
    # Purpose: make the blocking behavior unmistakably visible.
    # If Django signals were async, the code after save() would not wait here.
    # But it DOES wait — and that proves synchronous execution.
    print("[SIGNAL] Sleeping for 2 seconds inside the signal...")
    time.sleep(2)

    print("[SIGNAL] Signal handler has finished.")
    print("---")

