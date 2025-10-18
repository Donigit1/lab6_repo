from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text=None, start=None, end=None, replace_with="BIP"):
    if text is None:
        text = input("text: ")
    if start is None:
        start = int(input("start: "))
    if end is None:
        end = int(input("end: "))

    engine = AnonymizerEngine()
    result = engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=start, end=end, score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": replace_with})},
    )
    return result

if __name__ == "__main__":
    out = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")
    print(f"text: {out.text}")
    print("items:")
    print("[")
    for item in out.items:
        print(
            f"    {{'start': {item.start}, 'end': {item.end}, 'entity_type': '{item.entity_type}', 'text': '{item.text}', 'operator': '{item.operator}'}}"
        )
    print("]")
