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
  Links a vulnerability and one or more elements designating the latter as products not affected by the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VexNotAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {

  private String impactStatement;
  private ZonedDateTime impactStatementTime;
  private String justificationType;


}