# tv_show.py file
# main program
import tv

def main():
   # object creation
   television = ""
   tv1 = tv.__init__(television)

   # object usage
   tv1.show_status()
   tv1.turn_on()
   tv1.show_status()
   tv1.turn_off()
   tv1.show_status()


if __name__ == "__main__":
   main() 