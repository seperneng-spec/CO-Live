from app.core.sequencer import SequencerState


def test_sequencer_cycle():
    sequencer = SequencerState()
    sequencer.set_script(["hello", "world", "again"])

    assert sequencer.next() == "hello"
    assert sequencer.next() == "world"
    assert sequencer.next() == "again"
    assert sequencer.next() == "hello"


def test_sequencer_state_updates():
    sequencer = SequencerState()
    sequencer.set_mood("happy")
    sequencer.set_pose("wave")

    assert sequencer.mood == "happy"
    assert sequencer.pose == "wave"
