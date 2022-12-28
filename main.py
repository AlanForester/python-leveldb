import leveldb
import json


def main():
    db = leveldb.LevelDB("LevelDB/", create_if_missing=True)
    data = db.RangeIter()

    out = {}
    for key, value in data:
        decoded_val = value.decode("utf-8")
        clean_json = decoded_val.replace("\"", '"')
        encoded_json = json.loads(clean_json)

        print(encoded_json)
        out[key.decode("utf-8")] = encoded_json

    print(out['popupHasBeenSeen'], out['popupHasBeenSeen']['value'])


if __name__ == '__main__':
    main()
