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
  Provides a CVSS version 3 assessment for a vulnerability.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class CvssV3VulnAssessmentRelationship extends VulnAssessmentRelationship {

  private BigDecimal score;
  private String severity;
  private String vectorString;


}