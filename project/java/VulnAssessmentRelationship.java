package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Abstract ancestor class for all vulnerability assessments
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class VulnAssessmentRelationship extends Relationship {

  private ZonedDateTime withdrawnTime;
  private ZonedDateTime publishedTime;
  private SoftwareArtifact assessedElement;
  private Agent suppliedBy;
  private ZonedDateTime modifiedTime;

}