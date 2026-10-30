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
  Abstract ancestor class for all vulnerability assessments
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class VulnAssessmentRelationship extends Relationship {

  private SoftwareArtifact assessedElement;
  private String modifiedTime;
  private String publishedTime;
  private Agent suppliedBy;
  private String withdrawnTime;


}