package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Specifies an AI package and its associated information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIPackage extends Package {

  private String informationAboutTraining;
  private List<String> modelDataPreprocessing;
  private List<String> typeOfModel;
  private String safetyRiskAssessment;
  private List<DictionaryEntry> metricDecisionThreshold;
  private String useSensitivePersonalInformation;
  private EnergyConsumption energyConsumption;
  private String limitation;
  private List<DictionaryEntry> hyperparameter;
  private String autonomyType;
  private List<String> domain;
  private List<String> modelExplainability;
  private String informationAboutApplication;
  private List<DictionaryEntry> metric;
  private List<String> standardCompliance;

}