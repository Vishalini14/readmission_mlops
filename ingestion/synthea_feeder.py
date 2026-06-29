import subprocess, shutil, datetime, pathlib, sys

POP = int(sys.argv[1]) if len(sys.argv) > 1 else 500
DT  = datetime.date.today().isoformat()
SYN = pathlib.Path("synthea")
OUT = pathlib.Path(f"data/raw/source=synthea/dt={DT}")

def main():
    subprocess.run(
        ["./run_synthea", "-p", str(POP), "Massachusetts",
         "--exporter.csv.export", "true", "--exporter.fhir.export", "false"],
        cwd=SYN, check=True)
    OUT.mkdir(parents=True, exist_ok=True)
    src = SYN / "output" / "csv"
    for f in ["patients", "encounters", "conditions", "medications"]:
        shutil.copy(src / f"{f}.csv", OUT / f"{f}.csv")
    print(f"generated {POP} patients -> {OUT}")

if __name__ == "__main__":
    main()