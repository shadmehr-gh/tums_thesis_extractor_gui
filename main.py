import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter.ttk import Style
import webbrowser
import time

import input_checker
import lib_tums_ac_ir
import pdf_creator

global gui_app

global textbox_thesis_link
global textbox_page_count
global listbox_wait_time_options
global listbox_wait_time
global style_progress_bar
global progress_bar

biblioId, multimediaId, page_count, wait_time = "", "", "", ""

def main():
    # Version 4

    global gui_app
    gui_app = tkinter.Tk()
    gui_app.title("Thesis Extractor")
    gui_app.geometry('385x305')

    global style_window
    style_window = Style(gui_app)
    style_window.theme_use("default")

    menu_bar = tkinter.Menu(gui_app)

    more_menu = tkinter.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='More', menu=more_menu)
    more_menu.add_command(label='About', command=lambda: webbrowser.open("https://github.com/shadmehr-gh"))
    more_menu.add_separator()
    more_menu.add_command(label='Exit', command=gui_app.destroy)

    gui_app.config(menu=menu_bar)

    label_thesis_link = tkinter.Label(gui_app, text='Thesis Link:', width=50, anchor='w')
    label_thesis_link.place(x=10, y=10)
    #label_thesis_link.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)
    #label_thesis_link.grid(row=0, column=0)

    global textbox_thesis_link
    textbox_thesis_link = tkinter.Entry(gui_app, width=60)
    textbox_thesis_link.place(x=10, y=30)
    #textbox_thesis_link.pack(side=tkinter.TOP, padx=10, pady=0)
    #textbox_thesis_link.grid(row=1, column=0)
    textbox_thesis_link.insert(tkinter.END, "https://lib.tums.ac.ir/site/catalogue/fulltext/")

    label_thesis_link_example = tkinter.Label(gui_app, text='Ex: https://lib.tums.ac.ir/site/catalogue/fulltext/229225/170040401', width=55, fg="blue", anchor='w')
    label_thesis_link_example.place(x=10, y=50)
    #label_thesis_link_example.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)
    #label_thesis_link_example.grid(row=0, column=0)
    label_thesis_link_example.bind("<Enter>", on_hover)
    label_thesis_link_example.bind("<Leave>", on_leave)
    label_thesis_link_example.bind("<Button-1>", on_click_label_thesis_link_example)

    label_page_count = tkinter.Label(gui_app, text='Page Count:', width=50, anchor='w')
    label_page_count.place(x=10, y=80)
    #label_page_count.pack(side=tkinter.TOP, padx=5, pady=5)
    #label_page_count.grid(row=2, column=0)

    global textbox_page_count
    textbox_page_count = tkinter.Entry(gui_app, width=30)
    textbox_page_count.place(x=10, y=100)
    textbox_page_count.insert(tkinter.END, "0")
    #textbox_page_count.pack(side=tkinter.TOP, padx=10, pady=0)
    #textbox_page_count.grid(row=3, column=0)

    label_page_count_help = tkinter.Label(gui_app, text='Help: Please Enter the Thesis Page Numbers', width=55, fg="blue", anchor='w')
    label_page_count_help.place(x=10, y=120)
    #label_page_count_help.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)
    #label_page_count_help.grid(row=0, column=0)

    label_wait_time_options = tkinter.Label(gui_app, text='Wait Time:', width=50, anchor='w')
    label_wait_time_options.place(x=10, y=150)
    #label_wait_time_options.pack(side=tkinter.TOP, padx=5, pady=5)
    #label_wait_time_options.grid(row=4, column=0)

    global listbox_wait_time_options
    listbox_wait_time_options = []
    for i in range(5):
        listbox_wait_time_options.append(f'{i+1} sec')
    global listbox_wait_time
    listbox_wait_time = tkinter.ttk.Combobox(gui_app, values=listbox_wait_time_options)
    listbox_wait_time.current(2)
    listbox_wait_time.place(x=10, y=170)
    #listbox_wait_time.pack(side=tkinter.TOP, padx=5, pady=0)
    #listbox_wait_time.grid(row=4, column=0)

    label_wait_time_help = tkinter.Label(gui_app, text='Help: Please Enter the Wait Time (<2 Seconds is not Recommended!)', width=55, fg="blue", anchor='w')
    label_wait_time_help.place(x=10, y=192)
    #label_wait_time_help.pack(side=tkinter.TOP, fill=tkinter.BOTH, padx=5, pady=5)
    #label_wait_time_help.grid(row=0, column=0)

    label_driver = tkinter.Label(gui_app, text='Select Driver:', width=50, anchor='w')
    label_driver.place(x=10, y=220)
    #label_driver.pack(side=tkinter.TOP, padx=5, pady=5)
    #label_driver.grid(row=5, column=0)

    radiobutton_group = tkinter.IntVar()
    radiobutton_f = tkinter.Radiobutton(gui_app, text='Firefox', variable=radiobutton_group, value=0)
    radiobutton_f.place(x=90, y=220)
    #radiobutton_f.pack(side=tkinter.LEFT, padx=5, pady=5, anchor='w')
    #radiobutton_f.grid(row=5, column=1)
    radiobutton_c = tkinter.Radiobutton(gui_app, text='Chrome', variable=radiobutton_group, value=1, state="disabled")
    radiobutton_c.place(x=90, y=240)
    #radiobutton_c.pack(side=tkinter.LEFT, padx=5, pady=5, anchor='w')
    #radiobutton_c.grid(row=5, column=2)

    button_start = tkinter.Button(gui_app, text='Start', width=20)
    button_start.place(x=10, y=270)
    #button_start.pack(side=tkinter.TOP, padx=5, pady=5)
    #button_start.grid(row=6, column=0)
    button_start.bind("<Enter>", on_hover)
    button_start.bind("<Leave>", on_leave)
    button_start.bind("<Button-1>", on_click_button_start_pre)

    global style_progress_bar
    style_progress_bar = Style(gui_app)
    style_progress_bar.layout("LabeledProgressbar", [('LabeledProgressbar.trough', {'children': [('LabeledProgressbar.pbar', {'side': 'right', 'sticky': 'nswe'}), ("LabeledProgressbar.label", {"sticky": ""})], 'sticky': 'nswe'})])


    global progress_bar
    progress_bar = tkinter.ttk.Progressbar(gui_app, orient="horizontal", length=200, mode="indeterminate", maximum=100, value=0, style="LabeledProgressbar")
    progress_bar.place(x=170, y=273)
    #progress_bar.pack(side=tkinter.TOP, padx=5, pady=5)
    #progress_bar.grid(row=6, column=0)

    gui_app.mainloop()

    #biblioId, multimediaId, page_count = lib_tums_ac_ir.downloader()
    #pdf_creator.pdf_creator(biblioId, multimediaId, page_count)


def on_click_label_thesis_link_example(event):
    textbox_thesis_link.delete('0', tkinter.END)
    textbox_thesis_link.insert(tkinter.END, "https://lib.tums.ac.ir/site/catalogue/fulltext/229225/170040401")


def on_hover(event):
    event.widget.config(cursor="hand2")


def on_leave(event):
    event.widget.config(cursor="")


def on_click_button_start_pre(event):
    ### used this extra function to solve button stuck on press bug! ###
    gui_app.after(1000, on_click_button_start)


def on_click_button_start():
    progress_bar.start(10)
    #progress_bar.step(50)
    #progress_bar['value'] = 5
    #gui_app.update_idletasks()
    #gui_app.after(1000)
    #progress_bar.stop()

    style_progress_bar.configure("LabeledProgressbar", text="Checking Your Entered Data...")
    gui_app.update_idletasks()

    web_link = textbox_thesis_link.get()
    report = input_checker.id_checker(web_link)
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    page_count = textbox_page_count.get()
    report = input_checker.page_count_checker(page_count)
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    wait_time = str(int(listbox_wait_time_options.index(listbox_wait_time.get())) + 1)
    #print(wait_time)
    report = input_checker.wait_time_checker(wait_time)
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    biblioId = web_link[47:53]
    multimediaId = web_link[54:]

    gui_app.after(500)

    style_progress_bar.configure("LabeledProgressbar", text="Checking Your Operating System...")
    gui_app.update_idletasks()

    report = input_checker.os_checker()
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    gui_app.after(500)

    style_progress_bar.configure("LabeledProgressbar", text="Starting Robot. Please Wait...")
    gui_app.update()

    lib_tums_ac_ir.folder_preparator()

    gui_app.after(500)

    report = lib_tums_ac_ir.downloader(web_link, biblioId, page_count, wait_time)
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    gui_app.after(1000)

    style_progress_bar.configure("LabeledProgressbar", text="Building PDF File. Please Wait...")
    gui_app.update()

    gui_app.after(1000)

    report, pdf_path = pdf_creator.pdf_creator(biblioId, multimediaId, page_count)
    if not report == "Pass":
        tkinter.messagebox.showerror("Error", report)
        style_progress_bar.configure("LabeledProgressbar", text="")
        gui_app.update()
        progress_bar.stop()
        return

    gui_app.after(1000)

    style_progress_bar.configure("LabeledProgressbar", text="Task Finished.")
    gui_app.update()

    gui_app.after(500)

    progress_bar.stop()
    tkinter.messagebox.showinfo("Result", "Task Finished. " + f"Final PDF Saved in the {pdf_path} Address.")

    gui_app.update()

if __name__ == '__main__':
    main()
