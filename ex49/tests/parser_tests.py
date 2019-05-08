from nose.tools import *
from ex49.parser import *
from ex49.lexicon import *


def test_Sentence_class():
    a = ("noun", "bear")
    b = ("verb", "eat")
    c = ("noun", "apple")
    d = Sentence(a, b, c)
    assert_equal(d.subject, "bear")
    assert_equal(d.verb, "eat")
    assert_equal(d.object, "apple")


def test_peek_function():
    assert_equal(peek(lexicon.scan("the")), "stop")
    assert_equal(peek(lexicon.scan("go")), "verb")
    assert_equal(peek(lexicon.scan("bear")), "noun")
    assert_equal(peek(lexicon.scan("north")), "direction")
    assert_equal(peek(lexicon.scan("1234")), "number")
    assert_equal(peek(lexicon.scan("ASDK")), "error")
    assert_equal(peek([]), None)
    assert_equal(peek(lexicon.scan("the bear")), "stop")

def test_match_function():
    assert_equal(match(lexicon.scan("the"), "stop"), ("stop", "the"))
    assert_equal(match(lexicon.scan("go"), "verb"), ("verb", "go"))
    assert_equal(match(lexicon.scan("bear"), "noun"), ("noun", "bear"))
    assert_equal(match(lexicon.scan("north"), "direction"), ("direction", "north"))
    assert_equal(match(lexicon.scan("1234"), "number"), ("number", 1234))
    assert_equal(match(lexicon.scan("ASDK"), "error"), ("error", "ASDK"))
    assert_equal(match([], "stop"), None)
    assert_equal(match(lexicon.scan("go"), "stop"), None)
    assert_equal(match(lexicon.scan("the bear"), "stop"), ("stop", "the"))

def test_skip_function():
    a = lexicon.scan("the 1234")
    skip(a, "stop")
    assert_equal(a, [("number", 1234)])
    
    b = lexicon.scan("go 1234")
    skip(b, "verb")
    assert_equal(b, [("number", 1234)])
    
    c = lexicon.scan("bear 1234")
    skip(c, "noun")
    assert_equal(c, [("number", 1234)])
    
    d = lexicon.scan("north 1234")
    skip(d, "direction")
    assert_equal(d, [("number", 1234)])
    
    e = lexicon.scan("1234 1234")
    skip(e, "number")
    assert_equal(e, [])
    
    f = lexicon.scan("ASDK 1234")
    skip(f, "error")
    assert_equal(f, [("number", 1234)])
    
    g = lexicon.scan("the 1234")
    skip(g, "number")
    assert_equal(g, [("stop", "the"), ("number", 1234)])

def test_parse_verb_function():
    assert_equal(parse_verb(lexicon.scan("the go")), ("verb", "go"))
    

def test_parse_object_function():
    assert_equal(parse_object(lexicon.scan("the north")), ("direction", "north"))
    assert_equal(parse_object(lexicon.scan("the bear")), ("noun", "bear"))

def test_parse_subject_function():
    a = Sentence(("noun", "player"), ("verb", "go"), ("direction", "left"))
    assert_equal((parse_subject(lexicon.scan("go left"), ("noun", "player"))).subject, a.subject)
    assert_equal((parse_subject(lexicon.scan("go left"), ("noun", "player"))).verb, a.verb)
    assert_equal((parse_subject(lexicon.scan("go left"), ("noun", "player"))).object, a.object)

def test_parse_sentence_function():
    a1 = Sentence(("noun", "player"), ("verb", "go"), ("direction", "left"))
    assert_equal(parse_sentence(lexicon.scan("go left")).subject, a1.subject)
    assert_equal(parse_sentence(lexicon.scan("go left")).verb, a1.verb)
    assert_equal(parse_sentence(lexicon.scan("go left")).object, a1.object)
    
    a2 = Sentence(("noun", "bear"), ("verb", "stop"), ("noun", "door"))
    assert_equal(parse_sentence(lexicon.scan("bear stop at the door")).subject, a2.subject)
    assert_equal(parse_sentence(lexicon.scan("bear stop at the door")).verb, a2.verb)
    assert_equal(parse_sentence(lexicon.scan("bear stop at the door")).object, a2.object)

def test_fails():
    assert_raises(Exception, parse_verb, [("stop", "the"), ("noun", "honey")])
    assert_raises(Exception, parse_object, [("stop", "the"), ("verb", "run")])
    assert_raises(Exception, parse_sentence, [("stop", "the"), ("number", 1234)])