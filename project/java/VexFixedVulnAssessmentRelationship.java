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
  Links a vulnerability and elements representing products (in the VEX sense) where a fix has been applied and are no longer affected.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class VexFixedVulnAssessmentRelationship extends VexVulnAssessmentRelationship {



}