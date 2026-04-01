package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Class that describes a build instance of software/artifacts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Build extends Element {

  private String buildType;
  private ZonedDateTime buildEndTime;
  private String buildId;
  private List<Hash> configSourceDigest;
  private ZonedDateTime buildStartTime;
  private List<String> configSourceUri;
  private List<DictionaryEntry> parameter;
  private List<String> configSourceEntrypoint;
  private List<DictionaryEntry> environment;

}