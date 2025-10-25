# part 4

def main():
    acc = 0
    
    try:
        f = open('/host/Assignment2/comp4651-25fall-assignment-2/guest_program.txt', 'r')
        for line in f:
            instruction = line.strip()
            if not instruction:
                continue
            
            parts = instruction.split()
            cmd = parts[0]
            
            if cmd == 'add':
                value = int(parts[1])
                print("[Guest] Executing: {0}".format(instruction))
                acc += value
                
            elif cmd == 'print':
                print("[Guest] Executing: {0}".format(instruction))
                print("Accumulator value: {0}".format(acc))
                
            elif cmd == 'scan_disk':
                print("[VMM] Trapped privileged instruction 'scan_disk', emulating...")
                
            elif cmd == 'halt':
                print("[VMM] Trapped privileged instruction 'halt'. Halting guest.")
                # break the execution loop
                break
                
            else:
                print("[VMM] Error: Unknown instruction '{0}'".format(instruction))
                break
        
        f.close()
                
    except IOError:
        print("Error: guest_program.txt not found")
        return 1
    except Exception as e:
        print("Error: {0}".format(e))
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())

