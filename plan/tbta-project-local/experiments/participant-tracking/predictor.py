"""
Participant Tracking Prediction for TBTA Feature Reproduction
Experiment 001: Master/Servant Relationships (MAT 24:46-47)

This module implements the prediction algorithm for participant tracking values
as defined in experiment-001.md
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Set
from enum import Enum


class ParticipantTrackingValue(Enum):
    """TBTA Participant Tracking feature values"""
    FIRST_MENTION = "First Mention"
    ROUTINE = "Routine"
    INTEGRATION = "Integration"
    EXITING = "Exiting"
    RESTAGING = "Restaging"
    OFFSTAGE = "Offstage"
    GENERIC = "Generic"
    INTERROGATIVE = "Interrogative"
    FRAME_INFERABLE = "Frame Inferable"


@dataclass
class Entity:
    """Representation of a discourse entity"""
    text: str  # The actual text (word/phrase)
    verse_ref: str  # e.g., "MAT 24:46"
    part_of_speech: str  # NP, NP-pron, Noun, Pronoun, etc.
    position: int  # Character position in verse text
    is_pronoun: bool = False
    is_possessive: bool = False
    is_demonstrative: bool = False
    first_appearance_verse: Optional[str] = None  # Track across verses


@dataclass
class EntityReference:
    """A reference to an entity in discourse"""
    entity: Entity
    verse_ref: str
    prediction: ParticipantTrackingValue
    confidence: str  # "High", "Medium", "Low"
    reasoning: str


class ParticipantTrackingPredictor:
    """
    Predicts TBTA Participant Tracking values for entities in Bible verses.

    Algorithm steps:
    1. Context analysis - identify entities and relationships
    2. First appearance detection - new vs established
    3. Routine vs exiting decision - continuity analysis
    4. Frame inferable detection - implicit entities
    5. Special cases - interrogative, generic, etc.
    """

    def __init__(self):
        """Initialize the predictor with discourse context"""
        self.entity_registry: Dict[str, Entity] = {}
        self.references: List[EntityReference] = []
        self.narrative_context: Dict[str, str] = {}

    def register_context(self, verse_ref: str, narrative_type: str = "narrative"):
        """
        Register narrative context for a verse.

        Args:
            verse_ref: Bible reference (e.g., "MAT 24:46")
            narrative_type: Type of discourse (narrative, parable, dialogue, etc.)
        """
        self.narrative_context[verse_ref] = narrative_type

    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the registry"""
        self.entity_registry[entity.text.lower()] = entity

    def step1_context_analysis(self, verse_text: str, verse_ref: str) -> Dict[str, Entity]:
        """
        Step 1: Identify all noun phrases and pronouns, build entity reference chains.

        This is a simplified version - in real implementation would use NLP tagging.
        """
        # Manual annotation for MAT 24:46-47 (would use NLP parser in production)
        entities = {}

        # For this test case, we'll manually identify entities
        if verse_ref == "MAT 24:46":
            entities = {
                "servant": Entity(
                    text="servant",
                    verse_ref=verse_ref,
                    part_of_speech="NP",
                    position=15,
                    is_pronoun=False
                ),
                "lord": Entity(
                    text="lord",
                    verse_ref=verse_ref,
                    part_of_speech="NP",
                    position=44,
                    is_pronoun=False
                ),
                "he": Entity(
                    text="he",
                    verse_ref=verse_ref,
                    part_of_speech="Pronoun",
                    position=70,
                    is_pronoun=True
                ),
            }
        elif verse_ref == "MAT 24:47":
            entities = {
                "he": Entity(
                    text="he",
                    verse_ref=verse_ref,
                    part_of_speech="Pronoun",
                    position=35,
                    is_pronoun=True
                ),
                "him": Entity(
                    text="him",
                    verse_ref=verse_ref,
                    part_of_speech="Pronoun",
                    position=55,
                    is_pronoun=True
                ),
                "goods": Entity(
                    text="goods",
                    verse_ref=verse_ref,
                    part_of_speech="NP",
                    position=85,
                    is_pronoun=False,
                    is_possessive=True
                ),
            }

        for key, entity in entities.items():
            self.add_entity(entity)

        return entities

    def step2_first_appearance_detection(
        self, entity: Entity, all_previous_verses: List[str]
    ) -> bool:
        """
        Step 2: Detect if entity is appearing for the first time.

        Returns:
            True if first appearance, False if established entity
        """
        # Check if entity appears in known previous context
        entity_lower = entity.text.lower()

        # In a parable, "servant" generically introduced earlier but "that servant" is specific
        if entity.is_demonstrative:
            return True  # Demonstrative + noun = typically First Mention in parables

        # Check pronouns - they continue established entities
        if entity.is_pronoun:
            return False  # Pronouns refer to established entities

        # Check if in previous verses (would need full discourse chain)
        # For now, simplified: if mentioned in immediately preceding verses, it's Routine
        if "MAT 24:45" in all_previous_verses and entity.text.lower() in ["lord", "servant"]:
            return False  # These were introduced in 24:45

        return True

    def step3_routine_vs_exiting(
        self, entity: Entity, verse_ref: str, next_verse: Optional[str] = None
    ) -> ParticipantTrackingValue:
        """
        Step 3: For established entities, determine if Routine or Exiting.

        Returns:
            ParticipantTrackingValue indicating Routine or Exiting
        """
        # Check if entity is actively engaged in narrative
        # In MAT 24:46-47, both servant and lord are actively involved

        if entity.is_pronoun:
            return ParticipantTrackingValue.ROUTINE

        # If entity is the focus of narrative action, it's Routine
        if entity.text.lower() in ["servant", "lord"]:
            return ParticipantTrackingValue.ROUTINE

        # If entity is mentioned but passive, might be Exiting or Offstage
        return ParticipantTrackingValue.ROUTINE

    def step4_frame_inferable_detection(self, entity: Entity) -> bool:
        """
        Step 4: Detect implicit/frame-inferable entities.

        Returns:
            True if entity should be marked Frame Inferable
        """
        # Possessive constructions are Frame Inferable
        if entity.is_possessive:
            return True

        # Kinship/relationship nouns might be Frame Inferable
        if entity.text.lower() in ["father", "daughter", "son", "daughter", "goods", "master"]:
            return True

        # Entities understood through cultural context
        # (In a master/servant story, the "goods" are Frame Inferable)

        return False

    def step5_special_cases(self, entity: Entity, verse_text: str) -> Optional[ParticipantTrackingValue]:
        """
        Step 5: Check for special cases.

        Returns:
            Special case value if applicable, None otherwise
        """
        # Check for interrogative context
        if "?" in verse_text:
            return ParticipantTrackingValue.INTERROGATIVE

        # Check for generic/non-specific use
        if entity.text.lower() in ["man", "woman", "servant"] and not entity.is_demonstrative:
            # Would check for article/determiner in full implementation
            pass

        return None

    def predict(self, entity: Entity, verse_ref: str, verse_text: str) -> EntityReference:
        """
        Main prediction method - orchestrates all steps.

        Returns:
            EntityReference with prediction and reasoning
        """
        # Step 5: Check special cases first
        special = self.step5_special_cases(entity, verse_text)
        if special:
            return EntityReference(
                entity=entity,
                verse_ref=verse_ref,
                prediction=special,
                confidence="High",
                reasoning=f"Special case: {special.value}"
            )

        # Step 2: First appearance detection
        # Simplified - would track full discourse history
        all_previous = ["MAT 24:45"] if verse_ref == "MAT 24:46" else ["MAT 24:45", "MAT 24:46"]
        is_first = self.step2_first_appearance_detection(entity, all_previous)

        # Step 4: Frame Inferable detection
        is_frame_inferable = self.step4_frame_inferable_detection(entity)

        if is_frame_inferable:
            reasoning = f"Possessive/implicit entity: '{entity.text}' is understood from context"
            prediction = ParticipantTrackingValue.FRAME_INFERABLE
            confidence = "Medium"
        elif is_first:
            reasoning = f"New entity introduced: '{entity.text}' appears for first time in this specific context"
            prediction = ParticipantTrackingValue.FIRST_MENTION
            confidence = "High"
        else:
            # Step 3: Routine vs Exiting
            prediction = self.step3_routine_vs_exiting(entity, verse_ref)
            reasoning = f"Established entity: '{entity.text}' continues from previous context"
            confidence = "High"

        # Record reference
        ref = EntityReference(
            entity=entity,
            verse_ref=verse_ref,
            prediction=prediction,
            confidence=confidence,
            reasoning=reasoning
        )
        self.references.append(ref)

        return ref

    def predict_verse(self, verse_ref: str, verse_text: str) -> List[EntityReference]:
        """
        Predict participant tracking for all entities in a verse.

        Returns:
            List of EntityReference objects with predictions
        """
        # Step 1: Context analysis
        entities = self.step1_context_analysis(verse_text, verse_ref)

        # Predict for each entity
        predictions = []
        for entity in entities.values():
            ref = self.predict(entity, verse_ref, verse_text)
            predictions.append(ref)

        return predictions

    def get_results_summary(self) -> str:
        """Return a formatted summary of all predictions"""
        summary = "Participant Tracking Predictions Summary\n"
        summary += "=" * 60 + "\n\n"

        by_verse = {}
        for ref in self.references:
            if ref.verse_ref not in by_verse:
                by_verse[ref.verse_ref] = []
            by_verse[ref.verse_ref].append(ref)

        for verse_ref in sorted(by_verse.keys()):
            summary += f"\n{verse_ref}\n"
            summary += "-" * 40 + "\n"

            for ref in by_verse[verse_ref]:
                summary += f"\nEntity: {ref.entity.text}\n"
                summary += f"  Prediction: {ref.prediction.value}\n"
                summary += f"  Confidence: {ref.confidence}\n"
                summary += f"  Reasoning: {ref.reasoning}\n"

        return summary


def main():
    """Test the predictor with MAT 24:46-47"""
    predictor = ParticipantTrackingPredictor()

    # Register verses
    predictor.register_context("MAT 24:46", "parable")
    predictor.register_context("MAT 24:47", "parable")

    # Predict for MAT 24:46
    verse_46 = "Blessed is that servant whom his lord when he cometh shall find so doing."
    predictions_46 = predictor.predict_verse("MAT 24:46", verse_46)

    # Predict for MAT 24:47
    verse_47 = "Verily I say unto you, That he shall make him ruler over all his goods."
    predictions_47 = predictor.predict_verse("MAT 24:47", verse_47)

    # Print results
    print(predictor.get_results_summary())

    # Print detailed predictions table
    print("\n\nDetailed Predictions Table\n")
    print(f"{'Verse':<12} | {'Entity':<15} | {'Prediction':<20} | {'Confidence':<10}")
    print("-" * 60)

    for ref in predictor.references:
        print(f"{ref.verse_ref:<12} | {ref.entity.text:<15} | {ref.prediction.value:<20} | {ref.confidence:<10}")

    print("\n")


if __name__ == "__main__":
    main()
