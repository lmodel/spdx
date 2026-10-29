package example;

/* metamodel_version: 1.12.0 */
/* version: 3.0.1 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  Specifies an AI package and its associated information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AIPackage extends Package {

  private String autonomyType;
  private List<String> domain;
  private EnergyConsumption energyConsumption;
  private List<DictionaryEntry> hyperparameter;
  private String informationAboutApplication;
  private String informationAboutTraining;
  private String limitation;
  private List<DictionaryEntry> metric;
  private List<DictionaryEntry> metricDecisionThreshold;
  private List<String> modelDataPreprocessing;
  private List<String> modelExplainability;
  private String safetyRiskAssessment;
  private List<String> standardCompliance;
  private List<String> typeOfModel;
  private String useSensitivePersonalInformation;


}