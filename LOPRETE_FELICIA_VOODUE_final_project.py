import tkinter
import tkinter.messagebox
import pickle
import datetime

root=tkinter.Tk()
root.title("VooDoo")
root.geometry('600x700')
root.configure(bg='#55556B')


frame_tasks=tkinter.Frame(root,bg='#55556B')
frame_tasks.pack()

top_label=tkinter.Label(frame_tasks, text="VooDue app", font='times_new_roman, 25 bold', width=10,border=5, bg="mistyrose4")
top_label.pack()


listbox_tasts=tkinter.Listbox(frame_tasks, height=3, width=50)
listbox_tasts.pack()

entry_task=tkinter.Entry(root, width=50)
entry_task.pack()

sug=tkinter.Label(root,text="Suggessted tasks", font="arial, 16")
sug.pack()


n=4
def my_fun(k):
    
    for I in range(n):
        e=tkinter.Button(root,text=I, command=lambda k=I:my_fun(k))
        e.pack()

my_str=tkinter.StringVar()
l1=tkinter.Entry(root, textvariable=my_str, width=20)
l1.pack()
def show_suggs(suggs):
    my_str.set(suggs)

suggessted_tasks=[("Do homework"),("Practice Python" ),("Meet with advisor"),( "Study")]

var=0

for suggs in suggessted_tasks:
   
    button=tkinter.Button(root,text=suggs, command=lambda sug=suggs:show_suggs(sug))
    button.pack(padx=5, pady=var, )
    var+=1



class add_task:
    def __init__(self) :
        
        task=entry_task.get()
        if task!="":
            listbox_tasts.insert(tkinter.END, task)
            entry_task.delete(0,tkinter.END)
        else:
            tkinter.messagebox.showwarning("ERROR","Please enter a task.")


class delete_task:
    def __init__(self) :
        tasks=entry_task.delete(tkinter.END)
        if tasks!="":
            listbox_tasts.delete(tkinter.ACTIVE, tasks)
        else:
            tkinter.messagebox.showwarning("There is nothing to delete")

class load_tasks:
    def __init__(self) :
        load=pickle.load(open('tasks.txt', 'rb'))
        for task in load:
            listbox_tasts.insert(tkinter.END,task)
class save_tasks:
    def __init__(self) :
        save= listbox_tasts.get(0,listbox_tasts.size())
        pickle.dump(save,open("tasks.txt", 'wb'))





button_add_task=tkinter.Button(frame_tasks, text='Add Task', font='arial, 15', width=48,command=add_task)
button_add_task.pack(padx=10, pady=10)

button_delete_task=tkinter.Button(frame_tasks, text='Delete Task', font='arial, 15', width=48,command=delete_task)
button_delete_task.pack(padx=10, pady=10)

button_load_task=tkinter.Button(frame_tasks, text='Load Task', font='arial, 15', width=48,command=load_tasks)
button_load_task.pack(padx=10, pady=10)

button_save_task=tkinter.Button(frame_tasks, text='Save Task', font='arial, 15', width=48,command=save_tasks)
button_save_task.pack(padx=10, pady=10)













root.mainloop()