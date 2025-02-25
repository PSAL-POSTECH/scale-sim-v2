import argparse
from scalesim.scale_sim import scalesim
import os 

def main(config, topo_path, top, is_gemm):
    result_list = dict()
    
    for name in os.listdir(topo_path):
        if "csv" not in name:
            continue
        topo = os.path.join(topo_path, name)
        
        s = scalesim(save_disk_space=False, verbose=True, config=config, topology=topo, input_type_gemm=is_gemm)
        s.run_scale(top_path=top)
        total_cycles = s.get_total_cycles()
        result_list[name] = total_cycles
    
    for name, result in result_list.items():
        print(f"{name} : {result} cycle")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Scale-Sim with configurable paths")
    parser.add_argument("--config", type=str, required=True, help="Path to the configuration file")
    parser.add_argument("--topo_path", type=str, required=True, help="Path to the topology directory")
    parser.add_argument("--top", type=str, default="validation_result", help="Output directory for results")
    
    args = parser.parse_args()
    main(args.config, args.topo_path, args.top, "gemm" in args.topo_path or "bert" in args.topo_path)
