from model_context.local_object import GlobalObjectForContext


def test_context_object_accepts_question():
    obj = GlobalObjectForContext(
        id_global="g1",
        etiqueta="Andrea",
        confianza=0.8,
        question="Hola",
    )
    assert obj.question == "Hola"
