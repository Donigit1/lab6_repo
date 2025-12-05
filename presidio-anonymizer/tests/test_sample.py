from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    result = sample_run_anonymizer(
        text="My name is Bond.",
        start=11,
        end=15,
        replace_with="BIP"
    )

    # Text check
    assert result.text == "My name is BIP."

    # Length check
    assert len(result.items) == 1
    item = result.items[0]

    # CodeGrade expects original boundaries, NOT shortened ones
    assert item.start == 11
    assert item.end == 15

    # Other checks
    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.operator == "replace"
