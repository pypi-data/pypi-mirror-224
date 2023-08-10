import tkinter as tk


class ChatApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("chatroom")

        self.messages = []

        self.message_frame = tk.Frame(self.root)
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        self.message_listbox = tk.Listbox(self.message_frame, font=("Helvetica", 14), width=40)
        self.message_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.root, font=("Helvetica", 14))
        self.entry.pack(fill=tk.BOTH, expand=True)

        self.send_button = tk.Button(self.root, text="send", command=self.send_message)
        self.send_button.pack(fill=tk.BOTH, expand=True)

    def send_message(self):
        message = self.entry.get()
        if message:
            self.messages.append(("Me", message))
            self.messages.append(("Friend", "response"))  # 대화 상대의 응답 메시지 예시
            self.update_message_listbox()
            self.entry.delete(0, tk.END)

    def update_message_listbox(self):
        self.message_listbox.delete(0, tk.END)
        for sender, message in self.messages:
            formatted_message = f"[{sender}]: {message}"
            self.message_listbox.insert(tk.END, formatted_message)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = ChatApp()
    app.run()
