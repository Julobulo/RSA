import subprocess

def calculate_d(e, phi):
   def egcd(a, b):
      if a == 0:
         return (b, 0, 1)
      g, y, x = egcd(b%a,a)
      return (g, x - (b//a) * y, y)

   def modinv(a, m):
      g, x, y = egcd(a, m)
      if g != 1:
         raise Exception('No modular inverse')
      return x%m

   return modinv(e, phi)

def execute_python_file(file_path):
   try:
      completed_process = subprocess.run(['python', file_path], capture_output=True, text=True)
      if completed_process.returncode == 0:
         return int(completed_process.stdout)
      else:
         print(f"Error: Failed to execute '{file_path}' .")
         print("Error output:")
         print(completed_process.stderr)
   except FileNotFoundError:
      print(f"Error: The file '{file_path}'  does not exist.")

def calculateKeys():
   # Calculate P, Q, n, and phi
   P = execute_python_file('.\calculate_prime_numbers.py')
   Q = execute_python_file('.\calculate_prime_numbers.py')
   n = P*Q
   phi = (P-1)*(Q-1)

   # Calculate E
   e = 65537

   # Calculate D
   d = calculate_d(e, phi)

   print("Public Key:", "\nn :\n", n, "\ne :\n", e)

   print("\nPrivate Key:", "\nd :\n", d)
    
   print("\n\nPlease keep the private key for you and only give the public key!")

YesOrNo = input("\nDo you want to generate rsa encryption keys? (y/n)")

while(YesOrNo != 'y' and YesOrNo != 'n'):
   print("Please enter a valid input!")
   YesOrNo = input("\nDo you want to generate rsa encryption keys? (y/n)")

if (YesOrNo == 'n'):
   print("\nIf you changed your mind, re-run the script!\n")
   print("Programm killed!\n")
   exit()
elif (YesOrNo == 'y'):
   print("\n calcultating keys...\n")
   calculateKeys()