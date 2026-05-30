import base64
import json
from pathlib import Path


def main() -> None:
    nb_path = Path(r"c:\Users\pipel\Downloads\analisis\proyectofinalanalisis\trabajo.ipynb")
    out_dir = nb_path.parent / "figuras_extraidas"
    out_dir.mkdir(exist_ok=True)

    notebook = json.loads(nb_path.read_text(encoding="utf-8"))
    count = 0

    for cell_index, cell in enumerate(notebook.get("cells", []), start=1):
        for output_index, output in enumerate(cell.get("outputs", []), start=1):
            image_data = output.get("data", {}).get("image/png")
            if not image_data:
                continue

            count += 1
            image_path = out_dir / f"fig_{count:03d}_cell{cell_index}_out{output_index}.png"
            image_path.write_bytes(base64.b64decode(image_data))

    print(f"exported {count} images to {out_dir}")


if __name__ == "__main__":
    main()