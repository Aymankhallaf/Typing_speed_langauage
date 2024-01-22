from tkinter import *
import time

window = Tk()
window.title("Typing speed test")
window.config(padx=10, pady=10)
window.minsize(width=600, height=400)

title_text = "Typing speed test"
subtitle_text = (f"How fast are your fingers? \r Do the one-minute typing test to find out!\ryou can use the paragraph "
                 f"under or enter another with any language,\ryou'll get your typing speed in CPM and WPM. Good luck!")
example_text = """A man can be arrested in
Italy for wearing a skirt in public."""

written_letters = []
written_words = []
time_required = 10  # in seconds
start_time = 0  # variable to store the start time


def get_example():
    example_text = example.get("1.0", END)
    words = example_text.split()
    return words


# time start when we press any key inside written text box
def start_writing(event=None):
    global start_time
    if start_time == 0:
        start_time = time.time()


# stop written and calculate words per minute(WPM) and character by second (CPS)
def stop():
    global start_time
    elapsed_time = time.time() - start_time
    # print("Time taken to write:", elapsed_time)
    get_written = written.get("1.0", END)
    written_words = get_written.split()
    written_letters = "".join(written_words)
    # calculate words per minute(WPM) and character by second (CPS)
    WPM = len(written_words) / (elapsed_time / 60)
    CPS = len(written_letters) / (elapsed_time)
    words=get_example()
    print(words)
    compare_words(l1=written_words, l2=words)
    result.config(
        text=f"WPM={round(WPM)} and CPS ={round(CPS)} \r {level(WPM)} \r {compare_words(l1=written_words, l2=words)} ")


# calculate the typing speed
def level(wpm):
    if wpm >= 41:
        return "you are typing fast(above the average)"
    else:
        return "you are to practicing more(above the average)"


# compare between the two text to find the wrong words
def compare_words(l1, l2):
    l3 = l2[0:len(l1)]
    wrong_words = [x for x in l1 if x not in l3]

    return F"you have {len(wrong_words)} words wrong {wrong_words} "


# reset
def reset():
    global start_time
    start_time = 0
    written.delete("1.0", END)
    result.config(text="result")
    window.after(time_required * 1000, stop)


# ui
app_title = Label(text=title_text, font=("Arial", 20, "bold"))
app_title.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

app_subtitle = Label(text=subtitle_text, font=("Arial", 16))
app_subtitle.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

example = Text(height=10, width=50, bg="light cyan")
example.grid(row=3, column=2, columnspan=3, rowspan=2, padx=10, pady=10)
example.insert("1.0", example_text)


written = Text(height=10, width=50, bg="light cyan")
written.grid(row=6, column=2, columnspan=3, rowspan=3, padx=10, pady=10)
written.bind("<Key>", start_writing)

result = Label(text="result", font=("Arial", 16, "bold"))
result.grid(row=10, column=2, columnspan=2, padx=10, pady=10)

reset_button = Button(text="Reset", command=reset, font=("Arial", 12, "bold"))
reset_button.grid(row=11, column=2, columnspan=2, pady=10)

# After the specified time, call the stop function
window.after(time_required * 1000, stop)

window.mainloop()
