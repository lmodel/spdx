package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Refers to any unit of content that can be associated with a distribution of
software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Package extends SoftwareArtifact {

  private String sourceInfo;
  private String homePage;
  private String downloadLocation;
  private String packageVersion;
  private String packageUrl;

}