package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Connects a vulnerability and an element designating the element as a product
affected by the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VexAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {

  private String actionStatement;
  private ZonedDateTime actionStatementTime;

}