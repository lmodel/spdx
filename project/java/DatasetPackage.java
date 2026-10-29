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
  Specifies a data package and its associated information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class DatasetPackage extends Package {

  private List<String> anonymizationMethodUsed;
  private String confidentialityLevel;
  private String dataCollectionProcess;
  private List<String> dataPreprocessing;
  private String datasetAvailability;
  private String datasetNoise;
  private Integer datasetSize;
  private List<String> datasetType;
  private String datasetUpdateMechanism;
  private String hasSensitivePersonalInformation;
  private String intendedUse;
  private List<String> knownBias;
  private List<DictionaryEntry> sensor;


}