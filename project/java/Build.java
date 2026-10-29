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
  Class that describes a build instance of software/artifacts.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Build extends Element {

  private ZonedDateTime buildEndTime;
  private String buildId;
  private ZonedDateTime buildStartTime;
  private URI buildType;
  private List<Hash> configSourceDigest;
  private List<String> configSourceEntrypoint;
  private List<URI> configSourceUri;
  private List<DictionaryEntry> environment;
  private List<DictionaryEntry> parameter;


}