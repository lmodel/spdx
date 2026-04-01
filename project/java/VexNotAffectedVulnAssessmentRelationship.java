package None;

/* metamodel_version: 1.7.0 */
/* version: 3.0.1 */
import java.util.List;
import lombok.*;

/**
  Links a vulnerability and one or more elements designating the latter as products
not affected by the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VexNotAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {

  private ZonedDateTime impactStatementTime;
  private String justificationType;
  private String impactStatement;

}