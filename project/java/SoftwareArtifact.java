package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  A distinct article or unit related to Software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class SoftwareArtifact extends Artifact {

  private List<String> attributionText;
  private String primaryPurpose;
  private List<String> additionalPurpose;
  private List<ContentIdentifier> contentIdentifier;
  private String copyrightText;

}