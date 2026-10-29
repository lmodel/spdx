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
  A distinct article or unit related to Software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class SoftwareArtifact extends Artifact {

  private List<String> additionalPurpose;
  private List<String> attributionText;
  private List<ContentIdentifier> contentIdentifier;
  private String copyrightText;
  private String primaryPurpose;


}