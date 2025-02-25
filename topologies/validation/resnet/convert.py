
def parse_line(line):
    parts = line.strip().split('x')
    if len(parts) == 6:
        return {
            "Ifmap height": parts[1],
            "Ifmap width": parts[2],
            "Filter height": parts[5].split("_")[0],
            "Filter width": parts[5].split("_")[0],
            "Channels": parts[3],
            "Num filters": parts[4],
            "Strides": parts[5].split("_")[1]
        }
    else:
        print("Wrong format...", parts)
    return None

def convert_to_csv(line, idx):
    parsed = parse_line(line)
    if parsed:
        layer_name = f"layer_{idx + 1}"
        print(",".join([layer_name, parsed["Ifmap height"], parsed["Ifmap width"], parsed["Filter height"], parsed["Filter width"], parsed["Channels"], parsed["Num filters"], parsed["Strides"]])+",")

if __name__ == "__main__":
    idx = 0
    while True:
        line = input()
        if line[0] == 'q':
            break
        convert_to_csv(line, idx)
        idx += 1
    print(f"Conversion complete.")
