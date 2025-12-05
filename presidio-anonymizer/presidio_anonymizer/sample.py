from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig

def sample_run_anonymizer(text: str, start: int, end: int):
    engine = AnonymizerEngine()
    return engine.anonymize(
        text=text,
        analyzer_results=[
            RecognizerResult(entity_type="PERSON", start=int(start), end=int(end), score=0.8)
        ],
        operators={"PERSON": OperatorConfig("replace", {"new_value": "BIP"})},
    )
    return result

if __name__ == "__main__":
    r = sample_run_anonymizer("My name is Bond.", 11, 15)
    print(f"text: {r.text}")
    print("items:")
    print("[")
    for it in r.items:
        print(
            f"    {{'start': {it.start}, 'end': {it.end}, "
            f"'entity_type': '{it.entity_type}', 'text': '{it.text}', "
            f"'operator': '{it.operator}'}}"
        )
    print("]")
