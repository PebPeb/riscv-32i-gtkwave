from Compiler_RV32I.rv32i.RV32I_Instr import *
import sys

def main():
  for line in sys.stdin:
    buf = line.strip()
    if buf:
      try:
        hx = int(buf, 16)
      except ValueError:
        continue  # skip invalid hex
      buf2 = parseHex_RV32I(buf)
      print(buf2)
      sys.stdout.flush()

if __name__ == "__main__":
  main()
