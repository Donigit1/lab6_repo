from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text, start, end, replace_with="BIP"):
    """
    Refactored version: NO input(), fully testable,
    takes parameters directly and RETURNS result.
    """
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
    # Example call required by the assignment
    out = sample_run_anonymizer("My name is Bond.", 11, 15, "BIP")

    print(f"text: {out.text}")
    print("items:")
    print("[")
    for item in out.items:
        print(
            f"    {{'start': {item.start}, 'end': {item.end}, 'entity_type': '{item.entity_type}', 'text': '{item.text}', 'operator': '{item.operator}'}}"
        )
    print("]")
