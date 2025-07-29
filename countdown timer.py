
import time
def countdown(t):
    """Countdown timer that prints the time remaining every second."""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")
import winsound
def buzz():
    """Buzz sound when the timer reaches zero."""
    frequency = 1000  # Set Frequency To 1000 Hertz
    duration = 500    # Set Duration To 500 ms == 0.5 second
    winsound.Beep(frequency, duration)
def start_timer(seconds):
    """Start the countdown timer and play a sound when it ends."""
    print(f"Starting timer for {seconds} seconds...")
    countdown(seconds)
    buzz()
    print("Timer finished!")
if __name__ == "__main__":
    try:
        seconds = int(input("Enter the time in seconds for the countdown timer: "))
        if seconds < 0: 
            print("Please enter a positive number.")
        else:
            start_timer(seconds)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
print("would you like to set another timer? (yes/no)")
while True:
    response = input().lower()
    if response == "yes":
        try:
            seconds = int(input("Enter the time in seconds for the countdown timer: "))
            if seconds < 0: 
                print("Please enter a positive number.")
            else:
                start_timer(seconds)
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    elif response == "no":
        print("Thank you for using the timer. Goodbye!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")
# This is a simple implementation of a countdown timer.
# The user can input the time in seconds, and the timer will count down to zero.
# When the timer reaches zero, it plays a sound to indicate that the time is up.
# The timer displays the time remaining in the format MM:SS.