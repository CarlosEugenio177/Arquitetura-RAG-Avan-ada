from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Document:
    id: str
    title: str
    text: str


def load_medical_manual_fragments() -> list[Document]:
    return [
        Document(
            id="DOC-001",
            title="Enxaqueca com aura",
            text=(
                "Paciente com cefaleia pulsátil unilateral, fotofobia, fonofobia "
                "e náuseas recorrentes sugere quadro compatível com enxaqueca. "
                "Avaliar fatores desencadeantes e sinais de alarme neurológico."
            ),
        ),
        Document(
            id="DOC-002",
            title="Crise hipertensiva",
            text=(
                "Elevação pressórica importante associada a cefaleia intensa, "
                "escotomas visuais, dor torácica ou dispneia exige investigação "
                "de lesão aguda de órgão-alvo."
            ),
        ),
        Document(
            id="DOC-003",
            title="Rinite alérgica",
            text=(
                "Prurido nasal, rinorreia hialina, espirros em salva e congestão "
                "nasal persistente são achados frequentes em rinite alérgica."
            ),
        ),
        Document(
            id="DOC-004",
            title="Asma brônquica",
            text=(
                "Dispneia episódica, sibilância, tosse noturna e opressão torácica "
                "podem indicar hiperresponsividade brônquica compatível com asma."
            ),
        ),
        Document(
            id="DOC-005",
            title="Pneumonia comunitária",
            text=(
                "Febre, tosse produtiva, taquipneia, dor pleurítica e estertores "
                "crepitantes sugerem pneumonia adquirida na comunidade."
            ),
        ),
        Document(
            id="DOC-006",
            title="Sinusite bacteriana",
            text=(
                "Dor facial, pressão em seios paranasais, rinorreia purulenta e "
                "piora após melhora inicial podem sugerir rinossinusite bacteriana."
            ),
        ),
        Document(
            id="DOC-007",
            title="Gastroenterite aguda",
            text=(
                "Diarreia aquosa, vômitos, cólicas abdominais e sinais de desidratação "
                "devem ser avaliados em suspeita de gastroenterite infecciosa."
            ),
        ),
        Document(
            id="DOC-008",
            title="Doença do refluxo gastroesofágico",
            text=(
                "Pirose retroesternal, regurgitação ácida e tosse crônica pós-prandial "
                "podem ocorrer na doença do refluxo gastroesofágico."
            ),
        ),
        Document(
            id="DOC-009",
            title="Infecção urinária baixa",
            text=(
                "Disúria, polaciúria, urgência miccional e dor suprapúbica sugerem "
                "cistite não complicada, especialmente na ausência de febre alta."
            ),
        ),
        Document(
            id="DOC-010",
            title="Pielonefrite",
            text=(
                "Febre, calafrios, dor lombar, náuseas e punho-percussão lombar "
                "positiva podem indicar pielonefrite aguda."
            ),
        ),
        Document(
            id="DOC-011",
            title="Diabetes mellitus descompensado",
            text=(
                "Poliúria, polidipsia, perda ponderal e hiperglicemia persistente "
                "sugerem descompensação metabólica por diabetes mellitus."
            ),
        ),
        Document(
            id="DOC-012",
            title="Hipoglicemia",
            text=(
                "Sudorese fria, tremores, palpitações, confusão mental e melhora "
                "após glicose são compatíveis com episódio hipoglicêmico."
            ),
        ),
        Document(
            id="DOC-013",
            title="Síndrome coronariana aguda",
            text=(
                "Dor torácica opressiva irradiada para membro superior esquerdo, "
                "diaforese, náuseas e dispneia exigem estratificação cardíaca urgente."
            ),
        ),
        Document(
            id="DOC-014",
            title="Insuficiência cardíaca",
            text=(
                "Dispneia aos esforços, ortopneia, edema periférico e turgência "
                "jugular podem sugerir congestão por insuficiência cardíaca."
            ),
        ),
        Document(
            id="DOC-015",
            title="Acidente vascular cerebral",
            text=(
                "Déficit neurológico focal súbito, assimetria facial, disartria "
                "e hemiparesia demandam avaliação imediata para evento cerebrovascular."
            ),
        ),
        Document(
            id="DOC-016",
            title="Meningite",
            text=(
                "Febre, rigidez de nuca, cefaleia intensa, fotofobia e alteração "
                "do nível de consciência compõem sinais sugestivos de meningite."
            ),
        ),
        Document(
            id="DOC-017",
            title="Anemia ferropriva",
            text=(
                "Astenia, palidez cutaneomucosa, tontura e ferritina reduzida "
                "podem indicar anemia ferropriva por deficiência de ferro."
            ),
        ),
        Document(
            id="DOC-018",
            title="Hipotireoidismo",
            text=(
                "Fadiga, intolerância ao frio, constipação, pele seca e bradicardia "
                "são manifestações frequentes de hipotireoidismo."
            ),
        ),
        Document(
            id="DOC-019",
            title="Dermatite atópica",
            text=(
                "Prurido cutâneo crônico, xerose, lesões eczematosas e história "
                "atópica familiar são comuns em dermatite atópica."
            ),
        ),
        Document(
            id="DOC-020",
            title="Anafilaxia",
            text=(
                "Urticária difusa, angioedema, broncoespasmo, hipotensão e sintomas "
                "gastrointestinais após exposição alergênica sugerem anafilaxia."
            ),
        ),
        Document(
            id="DOC-021",
            title="Vertigem vestibular",
            text=(
                "Vertigem rotatória, náuseas, nistagmo e piora com mudança de posição "
                "podem indicar acometimento vestibular periférico."
            ),
        ),
        Document(
            id="DOC-022",
            title="Cefaleia tensional",
            text=(
                "Cefaleia bilateral em aperto, intensidade leve a moderada e ausência "
                "de vômitos recorrentes favorecem hipótese de cefaleia tensional."
            ),
        ),
        Document(
            id="DOC-023",
            title="Bronquite aguda",
            text=(
                "Tosse persistente, expectoração, desconforto torácico e sibilos "
                "transitórios podem ocorrer em bronquite aguda viral."
            ),
        ),
        Document(
            id="DOC-024",
            title="Gastrite",
            text=(
                "Epigastralgia em queimação, náuseas, plenitude pós-prandial e "
                "desconforto abdominal alto podem sugerir gastrite."
            ),
        ),
    ]
