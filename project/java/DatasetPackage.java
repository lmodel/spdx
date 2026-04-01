package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Specifies a data package and its associated information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetPackage extends Package {

  private Integer datasetSize;
  private List<String> datasetType;
  private List<String> anonymizationMethodUsed;
  private String datasetUpdateMechanism;
  private String dataCollectionProcess;
  private List<String> knownBias;
  private List<DictionaryEntry> sensor;
  private List<String> dataPreprocessing;
  private String intendedUse;
  private String confidentialityLevel;
  private String datasetAvailability;
  private String hasSensitivePersonalInformation;
  private String datasetNoise;

}