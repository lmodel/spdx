package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Abstract ancestor class for all VEX relationships
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class VexVulnAssessmentRelationship extends VulnAssessmentRelationship {

  private String vexVersion;
  private String statusNotes;

}