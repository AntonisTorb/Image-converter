from pathlib import Path
from PIL import Image

def main():
    input_format = "webp"
    output_format = "png"

    cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    output_dir = cur_dir / "output"
    output_dir.mkdir(exist_ok=True)

    input_list = list(cur_dir.glob(f"*.{input_format}"))

    for image in input_list:
        print(f"Converting {image.name}")
        img_png = Image.open(image)
        img_png.save(f"{output_dir}\{str(image.name)[:-len(input_format)]}{output_format}")

    print("Done!")

if __name__ == "__main__":
    main()