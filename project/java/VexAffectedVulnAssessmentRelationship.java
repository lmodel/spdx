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
  Connects a vulnerability and an element designating the element as a product affected by the vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VexAffectedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {

  private String actionStatement;
  private String actionStatementTime;


}