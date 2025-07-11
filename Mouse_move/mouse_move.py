import pyautogui
import time
from datetime import datetime, timedelta
import tkinter as tk
import threading
import webbrowser, os
import psutil

pyautogui.FAILSAFE = False

class MoveMouse:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Move")
        self.master.resizable(width=False, height=False)
        self.master.geometry("300x250")

        self.title_label = tk.Label(self.master, text="Mouse Move",font=("Arial",20))
        self.title_label.pack(pady=10)

        self.timer_label = tk.Label(self.master, text="Starting..", font=("Arial", 12))
        self.timer_label.pack(pady=10)

        self.reset_initial = tk.Button(self.master, text="Initial", command=self.initial)
        self.reset_initial.pack(pady=5)

        self.run_button = tk.Button(self.master, text="Start", command=self.starting)
        self.run_button.pack(pady=5)

        self.resume_button = tk.Button(self.master, text="Resume", command=self.start)
        self.resume_button.pack(side=tk.LEFT, padx=30, pady=5)

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.RIGHT, padx=30, pady=5)

        self.resume_button.config(state="disabled")
        self.stop_button.config(state="disabled")

        self.running = False
        self.start_time = 120
        self.thread = None
        self.current_time = 6
        self.start_datetime = datetime.now()

        self.c3_profile_x, self.c3_profile_y = 3796, 108
        self.c3_logout_x, self.c3_logout_y = 3624, 466
        self.c3_user_x, self.c3_user_y = 4047, 1610
        self.c3_pass_x, self.c3_pass_y = 4047, 1667
        self.c3_login_x, self.c3_login_y = 4047, 1728

        self.yms_logout_x, self.yms_logout_y = 8073, 2256
        self.yms_user_x, self.yms_user_y = 7218, 3615
        self.yms_pass_x, self.yms_pass_y = 7218, 3641
        self.yms_login_x, self.yms_login_y = 7218, 3731
        self.yms_view_x, self.yms_view_y = 6456, 3519

        self.last_stop_time = None
        self.auto_restart_check()
        
    def initial(self):
        self.timer_label.config(text="Initial")

        self.rdp, self.connect = False, False
        os.startfile(r"C:\Users\mysliwiecm\OneDrive - NewCold Cooperatief UA\Desktop\MFCS.rdp")

        self.timeout = 30
        start_time = time.time()

        while time.time() - start_time < self.timeout:
            if "mstsc.exe" in (p.name() for p in psutil.process_iter()):
                print("RDP started.")
                break
            time.sleep(1)
        else:
            print("Timeout: RDP did not start.")
            exit(1)

        time.sleep(3)

        pyautogui.write('I-2505-GCS-1185')
        pyautogui.press('enter')

        print("Credentials sent.")

        time.sleep(2)

        webbrowser.open_new("https://www.c3reservations.com/newcold/app/login")
        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        webbrowser.open_new("https://newcold.ymshub.com/login")
        os.startfile("C:\Program Files\Axis Communications\AXIS Camera Station\Client Latest\AcsClient.exe")

    def starting(self):

        self.reset_initial.config(state="disabled")

        pyautogui.moveTo(self.c3_user_x, self.c3_user_y)
        pyautogui.click()
        pyautogui.write('piotrk1')

        pyautogui.moveTo(self.c3_pass_x, self.c3_pass_y)
        pyautogui.click()
        pyautogui.write('1')

        pyautogui.moveTo(self.c3_login_x, self.c3_login_y)
        pyautogui.click()

        time.sleep(1)
        
        pyautogui.moveTo(self.yms_user_x, self.yms_user_y)
        pyautogui.click()
        pyautogui.write('kutnoviewer')

        pyautogui.moveTo(self.yms_pass_x, self.yms_pass_y)
        pyautogui.click()
        pyautogui.write('NewPassword2502!')

        pyautogui.moveTo(self.yms_login_x, self.yms_login_y)
        pyautogui.click()

        time.sleep(5)
        
        pyautogui.moveTo(self.yms_view_x, self.yms_view_y)
        pyautogui.click()

        self.run_button.config(state="disabled")
        
        self.start()

    def move_mouse(self):

        c3_x, c3_y = 2977, 1922
        shift_c3_x, shift_c3_y = 4179, 1985
        refresh_c3_x, refresh_c3_y = 2637, 1111
        ts_x, ts_y = 6732, 1882
        yml_x, yml_y = 6465, 2215
        self.save_time = self.current_time

        if self.running:
            pyautogui.moveTo(ts_x, ts_y)
            pyautogui.click()

            pyautogui.moveTo(refresh_c3_x, refresh_c3_y)
            pyautogui.click()
            time.sleep(10)
            
            pyautogui.moveTo(c3_x, c3_y)
            pyautogui.click()
            pyautogui.scroll(self.save_time*(-155))
            
            pyautogui.moveTo(shift_c3_x, shift_c3_y)
            pyautogui.click()
            
            current_time = int(datetime.now().strftime("%H"))
            if current_time > self.save_time:
                self.save_time = current_time
            self.remaining_time = self.start_time

            pyautogui.moveTo(yml_x,yml_y)
            pyautogui.click()

            pyautogui.moveTo(100,500)
            pyautogui.click()
            
            self.update_timer()

            if datetime.now() >= self.start_datetime + timedelta(hours=12):
                self.timer_label.config(text="Restart")
                self.reset_accounts()
                self.start_datetime = datetime.now()

    def update_timer(self):
        if self.running and self.remaining_time > 0:
            self.timer_label.config(text=f"{self.remaining_time}s")
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        elif self.running:
            self.move_mouse()

    def reset_accounts(self):
        self.running = False

        pyautogui.moveTo(self.c3_profile_x, self.c3_profile_y)
        pyautogui.click()
        pyautogui.moveTo(self.c3_logout_x, self.c3_logout_y, 0.5)
        pyautogui.click()

        time.sleep(5)

        pyautogui.moveTo(self.c3_user_x, self.c3_user_y)
        pyautogui.click()
        pyautogui.write('piotrk1')

        pyautogui.moveTo(self.c3_pass_x, self.c3_pass_y)
        pyautogui.click()
        pyautogui.write('1')

        pyautogui.moveTo(self.c3_login_x, self.c3_login_y)
        pyautogui.click()

        time.sleep(1)

        pyautogui.moveTo(self.yms_logout_x, self.yms_logout_y)
        pyautogui.click()

        time.sleep(5)
        
        pyautogui.moveTo(self.yms_user_x, self.yms_user_y)
        pyautogui.click()
        pyautogui.write('kutnoviewer')

        pyautogui.moveTo(self.yms_pass_x, self.yms_pass_y)
        pyautogui.click()
        pyautogui.write('NewPassword2502!')

        pyautogui.moveTo(self.yms_login_x, self.yms_login_y)
        pyautogui.click()

        time.sleep(5)
        
        pyautogui.moveTo(self.yms_view_x, self.yms_view_y)
        pyautogui.click()

        self.running = True
        self.move_mouse()

    def start(self):
        self.stop_button.config(state="active")
        self.resume_button.config(state="disable")
        self.run_button.config(state="disabled")
        self.reset_initial.config(state="disabled")
        if not self.running:
            self.running = True
            self.remaining_time = self.start_time
            self.update_timer()

    def stop(self):
        self.resume_button.config(state="active")
        self.stop_button.config(state="disable")
        self.reset_initial.config(state="active")
        self.run_button.config(state="active")
        self.running = False
        self.timer_label.config(text="Stopped")
        self.last_stop_time = datetime.now()

    def auto_restart_check(self):
        if self.last_stop_time:
            if datetime.now() > self.last_stop_time + timedelta(seconds=60):
                self.last_stop_time = None
                self.start()
        self.master.after(1000, self.auto_restart_check)

if __name__ == "__main__":
    root = tk.Tk()
    app = MoveMouse(root)
    root.mainloop()
